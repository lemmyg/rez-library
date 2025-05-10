#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usdGeom/mesh.h>
#include <pxr/usd/usdGeom/xform.h>
#include <pxr/base/tf/diagnostic.h>
#include <iostream>

PXR_NAMESPACE_USING_DIRECTIVE

int main(int argc, char *argv[]) {
    // Initialize USD
    TfDiagnosticMgr::GetInstance().SetQuiet(true);

    // Create a new stage
    UsdStageRefPtr stage = UsdStage::CreateNew("test.usda");
    if (!stage) {
        std::cerr << "Failed to create stage" << std::endl;
        return 1;
    }

    // Create a simple mesh
    UsdGeomMesh mesh = UsdGeomMesh::Define(stage, SdfPath("/mesh"));
    
    // Set some basic mesh data
    VtVec3fArray points;
    points.push_back(GfVec3f(0, 0, 0));
    points.push_back(GfVec3f(1, 0, 0));
    points.push_back(GfVec3f(1, 1, 0));
    points.push_back(GfVec3f(0, 1, 0));
    
    VtIntArray faceVertexCounts;
    faceVertexCounts.push_back(4);
    
    VtIntArray faceVertexIndices;
    faceVertexIndices.push_back(0);
    faceVertexIndices.push_back(1);
    faceVertexIndices.push_back(2);
    faceVertexIndices.push_back(3);
    
    mesh.CreatePointsAttr().Set(points);
    mesh.CreateFaceVertexCountsAttr().Set(faceVertexCounts);
    mesh.CreateFaceVertexIndicesAttr().Set(faceVertexIndices);

    // Save the stage
    stage->Save();

    // Now try to load it back
    UsdStageRefPtr loadedStage = UsdStage::Open("test.usda");
    if (!loadedStage) {
        std::cerr << "Failed to load stage" << std::endl;
        return 1;
    }

    std::cout << "Successfully created and loaded USD stage" << std::endl;
    return 0;
}
